package com.pocketide.data.ai

import org.junit.Assert.assertFalse
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test

class BenchmarkNativePolicyTest {
    @Test
    fun onlyQuickGgufSchedulesNativeMicrobenchmark() {
        assertTrue(BenchmarkNativePolicy.isScheduled(ModelFormat.GGUF, BenchmarkDepth.QUICK))
        assertFalse(BenchmarkNativePolicy.isScheduled(ModelFormat.GGUF, BenchmarkDepth.DEEP))
        assertFalse(BenchmarkNativePolicy.isScheduled(ModelFormat.GGUF, BenchmarkDepth.SUSTAINED))
        assertFalse(BenchmarkNativePolicy.isScheduled(ModelFormat.PTE, BenchmarkDepth.QUICK))
    }

    @Test
    fun completedQuickGgufHasNoStatusMessage() {
        assertNull(
            BenchmarkNativePolicy.resultMessage(
                format = ModelFormat.GGUF,
                depth = BenchmarkDepth.QUICK,
                hasCalibration = true,
                hasResult = true,
            ),
        )
    }
}
