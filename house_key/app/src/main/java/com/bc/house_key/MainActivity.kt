package com.bc.house_key

import android.annotation.SuppressLint
import android.content.Context
import android.content.SharedPreferences
import khttp.get
import android.databinding.DataBindingUtil
import android.graphics.Typeface
import android.os.Bundle
import android.provider.Settings
import android.support.v7.app.AppCompatActivity
import android.widget.CompoundButton
import android.widget.Switch
import android.widget.TextView
import android.widget.ToggleButton
import rx.subscriptions.CompositeSubscription
import com.bc.house_key.ApiClient
import com.google.gson.FieldNamingPolicy
import com.google.gson.GsonBuilder
import com.google.gson.internal.bind.DateTypeAdapter
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.launch
import okhttp3.OkHttpClient
import okhttp3.Request
import retrofit.RestAdapter
import retrofit.android.AndroidLog
import retrofit.converter.GsonConverter
import java.util.*


class MainActivity : AppCompatActivity() {

    private val compositeSubscription = CompositeSubscription()

    private val ENDPOINT = "url"

    val gsonBuilder = GsonBuilder()
        .setFieldNamingPolicy(FieldNamingPolicy.LOWER_CASE_WITH_UNDERSCORES)
        .registerTypeAdapter(Date::class.java, DateTypeAdapter()).create()

    val restAdapter: RestAdapter = RestAdapter.Builder()
        .setEndpoint(ENDPOINT)
        .setConverter(GsonConverter(gsonBuilder))
        .setLogLevel(RestAdapter.LogLevel.FULL)
        .setLog(AndroidLog("=NETWORK="))
        .build();

    private lateinit var sharedPreferences: SharedPreferences

    @SuppressLint("WrongViewCast")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        //val textView = findViewById<TextView>(R.id.textView)
        val button =  findViewById<ToggleButton>(R.id.toggleButton)
        button.setOnCheckedChangeListener { _, isChacked: Boolean ->
            val client : OkHttpClient = OkHttpClient.Builder().build()
            /*
            button.setOnClickListener {
                val client: OkHttpClient = OkHttpClient.Builder().build()
            }
            */
            if (isChacked) {
                GlobalScope.launch{
                    val url : String = "url"
                    val request: Request = Request.Builder().url(url).build()
                    val response = client.newCall(request).execute()
                    val result: String? = response.body()?.string()
                    print(result)
                    response.close()
                    //val editor = sharedPreferences.edit()
                    //editor.putBoolean("toggleButton",true).apply()
                    //val islock : String = get(url).jsonObject.getString("islock")
                }
                button.setText("lock")
                Thread.sleep(1000)
                //textView.text = getString(R.string.lock)
            } else {
                GlobalScope.launch{
                    val url : String = "url"
                    val request: Request = Request.Builder().url(url).build()
                    val response = client.newCall(request).execute()
                    val result: String? = response.body()?.string()
                    print(result)
                    response.close()
                    //val editor = sharedPreferences.edit()
                    //editor.putBoolean("toggleButton",false).apply()
                    //val islock : String = get(url).jsonObject.getString("islock")
                }
                button.setText("lock")
                Thread.sleep(1000)
                //textView.text = "UnLocked"
            }
        }
    }
}
