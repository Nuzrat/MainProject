package com.example.garbagemanagementsystem;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.Preference;
import android.preference.PreferenceManager;
import android.view.View;
import android.widget.Button;

public class DriverHome extends AppCompatActivity {
    Button b1,b2,b3,b4,b5;
    SharedPreferences sh;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_driver_home);
        b1=findViewById(R.id.button3);
        b2=findViewById(R.id.button4);
        b3=findViewById(R.id.button5);
        b4=findViewById(R.id.button6);
        b5=findViewById(R.id.button8);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent ii=new Intent(getApplicationContext(),ViewAssignedPlaces.class);
                startActivity(ii);
            }
        });
        b2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent ii=new Intent(getApplicationContext(),UserSendNotification.class);
                startActivity(ii);
            }
        });
        b3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent ii=new Intent(getApplicationContext(),ViewPickUpNotification.class);
                startActivity(ii);
            }
        });
        b4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent ii=new Intent(getApplicationContext(),GenetateRouteInfo.class);
                startActivity(ii);
            }
        });
        b5.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent ii=new Intent(getApplicationContext(),login.class);
                startActivity(ii);
            }
        });
    }
}