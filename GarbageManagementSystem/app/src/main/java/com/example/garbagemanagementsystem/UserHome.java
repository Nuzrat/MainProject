package com.example.garbagemanagementsystem;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.View;
import android.widget.Button;

public class UserHome extends AppCompatActivity {
    Button b1;
    Button b2;
    Button b3;
    Button b4;
    Button b5;
    Button b6;
    Button b7;
    SharedPreferences sh;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_user_home);

        b2=findViewById(R.id.button10);
        b3=findViewById(R.id.button11);
        b4=findViewById(R.id.button12);
        b5=findViewById(R.id.button13);
        b6=findViewById(R.id.button14);
        b7=findViewById(R.id.button15);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());


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
                Intent ii=new Intent(getApplicationContext(),ViewProductBook.class);
                startActivity(ii);
            }
        });
        b5.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent ii=new Intent(getApplicationContext(),ViewAwarenessCampInfo.class);
                startActivity(ii);
            }
        });
        b6.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent ii=new Intent(getApplicationContext(),ViewVideos.class);
                startActivity(ii);
            }
        });
        b7.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent ii=new Intent(getApplicationContext(),login.class);
                startActivity(ii);
            }
        });

    }
}