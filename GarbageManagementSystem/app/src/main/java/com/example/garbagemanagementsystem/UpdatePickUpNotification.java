package com.example.garbagemanagementsystem;

import androidx.appcompat.app.AppCompatActivity;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class UpdatePickUpNotification extends AppCompatActivity {
    EditText e1;
    Button b1;
    SharedPreferences sh;
    String notification;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_update_pick_up_notification);
        e1=findViewById(R.id.editTextTextPersonName14);
        b1=findViewById(R.id.button18);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                notification = e1.getText().toString();
            }
        });
    }
}