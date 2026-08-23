package com.hzy.libp7zip;

/**
 * Local stub for the missing com.hzy.libp7zip.P7ZipApi
 * from the unavailable AndroidP7zip library.
 * 
 * NOTE: 7z extraction via command line will NOT work at runtime.
 * This stub only allows the project to compile.
 */
public class P7ZipApi {

    /**
     * Executes a 7z command. Stub returns -1 (error).
     * 
     * @param command the 7z command string
     * @return exit code, -1 indicates error/not implemented
     */
    public static int executeCommand(String command) {
        // Stub: real implementation requires native library
        return -1;
    }
}
