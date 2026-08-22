package com.hzy.lib7z;

/**
 * Local replacement for the missing com.hzy.lib7z.IExtractCallback
 * from the unavailable AndroidP7zip/AndroidUn7zip library.
 * 
 * The native library libp7zip.so is still packaged in the APK,
 * but the Java wrapper is no longer available in public repositories.
 * 
 * NOTE: 7z extraction functionality will NOT work at runtime.
 * This stub only allows the project to compile.
 */
public interface IExtractCallback {
    void onStart();
    void onGetFileNum(int fileNum);
    void onProgress(String name, long size);
    void onError(int errorCode, String message);
    void onSucceed();
}
