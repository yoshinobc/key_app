package com.bc.house_key

import android.telecom.Call
import retrofit.http.POST
import java.util.*
import com.bc.house_key.LockEntity
import com.bc.house_key.UnLockEntity


interface ApiClient {
    @POST("lock")
    public fun lock(): retrofit2.Call<LockEntity>

    @POST("unlock")
    public fun unlock(): retrofit2.Call<Array<UnLockEntity>>
}