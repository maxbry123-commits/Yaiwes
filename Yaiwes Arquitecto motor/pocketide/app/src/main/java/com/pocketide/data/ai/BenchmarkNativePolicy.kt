package com.pocketide.data.ai

/** Keeps the kernel microbenchmark separate from longer end-to-end benchmark modes. */
internal object BenchmarkNativePolicy {
    fun isScheduled(format: ModelFormat, depth: BenchmarkDepth): Boolean =
        format == ModelFormat.GGUF && depth == BenchmarkDepth.QUICK

    fun resultMessage(
        format: ModelFormat,
        depth: BenchmarkDepth,
        hasCalibration: Boolean,
        hasResult: Boolean,
    ): String? = when {
        format != ModelFormat.GGUF ->
            "Not applicable to PTE; performance is measured through ExecuTorch generation callbacks"
        depth != BenchmarkDepth.QUICK ->
            "Not run in Deep or Sustained mode; Quick is the dedicated native kernel microbenchmark"
        !hasCalibration ->
            "No calibrated GGUF thread profile was available for the native microbenchmark"
        !hasResult ->
            "Runtime returned no parseable native benchmark result"
        else -> null
    }
}
