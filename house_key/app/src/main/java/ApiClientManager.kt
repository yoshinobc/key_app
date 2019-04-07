package com.bc.house_key

import android.accessibilityservice.GestureDescription
import com.google.gson.Gson
import com.squareup.okhttp.OkHttpClient
import okhttp3.logging.HttpLoggingInterceptor
import retrofit2.Retrofit
import retrofit2.adapter.rxjava.RxJavaCallAdapterFactory
import retrofit2.converter.gson.GsonConverterFactory
import java.util.concurrent.TimeUnit

open class ApiClientManager{
    companion object {
        private const val ENDPOINT = ""

        val apiClient: ApiClient
            get() = Retrofit.Builder()
                .client(getClient())
                .baseUrl(ENDPOINT)
                .addConverterFactory(GsonConverterFactory.create(Gson()))
                .addCallAdapterFactory(RxJavaCallAdapterFactory.create())
                .build()
                .create(ApiClient::class.java)

        private fun getClient(): okhttp3.OkHttpClient {
            val client = okhttp3.OkHttpClient.Builder()
                .connectTimeout(120, TimeUnit.SECONDS)
                .readTimeout(120, TimeUnit.SECONDS)
                .addInterceptor(HttpLoggingInterceptor().apply {
                    level = HttpLoggingInterceptor.Level.BODY
                })
                return client.build()
        }
    }
}