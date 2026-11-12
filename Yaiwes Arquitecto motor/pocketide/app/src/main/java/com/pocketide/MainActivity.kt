package com.pocketide

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.lifecycle.ViewModelProvider
import androidx.lifecycle.viewmodel.compose.viewModel
import com.pocketide.ui.navigation.PocketIDENavGraph
import com.pocketide.ui.screens.editor.EditorViewModel
import com.pocketide.ui.theme.PocketIDETheme
import com.pocketide.ui.theme.ThemeViewModel

class MainActivity : ComponentActivity() {
    private lateinit var editorViewModel: EditorViewModel

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        editorViewModel = ViewModelProvider(this)[EditorViewModel::class.java]
        enableEdgeToEdge()
        setContent {
            val themeViewModel: ThemeViewModel = viewModel()
            val isDarkMode by themeViewModel.isDarkMode.collectAsState()

            PocketIDETheme(isDarkMode = isDarkMode) {
                Surface(
                    modifier = Modifier.fillMaxSize(),
                    color = MaterialTheme.colorScheme.background,
                ) {
                    PocketIDENavGraph(
                        themeViewModel = themeViewModel,
                        editorViewModel = editorViewModel,
                    )
                }
            }
        }
    }

    override fun onStart() {
        super.onStart()
        editorViewModel.onUiVisible()
    }

    override fun onStop() {
        if (!isChangingConfigurations) {
            editorViewModel.onUiHidden()
        }
        super.onStop()
    }
}
