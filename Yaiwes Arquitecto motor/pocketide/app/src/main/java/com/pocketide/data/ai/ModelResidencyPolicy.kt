package com.pocketide.data.ai

/**
 * Decides when reconstructable native model state should be released.
 *
 * A request made while inference is active remains pending until the work finishes. Returning
 * to the visible UI cancels a pending request so a foreground model is not immediately unloaded.
 */
internal class ModelResidencyPolicy {
    private var visible = true
    private var releasePending = false

    @Synchronized
    fun onUiVisible() {
        visible = true
        releasePending = false
    }

    @Synchronized
    fun onUiHidden() {
        visible = false
        releasePending = true
    }

    @Synchronized
    fun takeReleaseRequest(isBusy: Boolean): Boolean {
        if (visible || !releasePending || isBusy) return false
        releasePending = false
        return true
    }
}
