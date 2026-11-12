package com.pocketide.data.ai

import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

class ModelResidencyPolicyTest {
    @Test
    fun hiddenAndIdle_releasesOnce() {
        val policy = ModelResidencyPolicy()

        policy.onUiHidden()

        assertTrue(policy.takeReleaseRequest(isBusy = false))
        assertFalse(policy.takeReleaseRequest(isBusy = false))
    }

    @Test
    fun hiddenAndBusy_waitsUntilWorkFinishes() {
        val policy = ModelResidencyPolicy()

        policy.onUiHidden()

        assertFalse(policy.takeReleaseRequest(isBusy = true))
        assertTrue(policy.takeReleaseRequest(isBusy = false))
    }

    @Test
    fun returningVisible_cancelsPendingRelease() {
        val policy = ModelResidencyPolicy()

        policy.onUiHidden()
        policy.onUiVisible()

        assertFalse(policy.takeReleaseRequest(isBusy = false))
    }
}
