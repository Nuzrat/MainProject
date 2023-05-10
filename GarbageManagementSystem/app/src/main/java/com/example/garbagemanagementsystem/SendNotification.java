package com.example.garbagemanagementsystem;

import androidx.appcompat.app.AppCompatActivity;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;

public class SendNotification extends AppCompatActivity {
    Spinner s1;
    EditText e1;
    Button b1;
    SharedPreferences sh;
    String notification;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_send_notification);
        s1=findViewById(R.id.spinner);
        e1=findViewById(R.id.editTextTextPersonName4);
        b1=findViewById(R.id.button5);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                notification = e1.getText().toString();
            }
        });

    }
}