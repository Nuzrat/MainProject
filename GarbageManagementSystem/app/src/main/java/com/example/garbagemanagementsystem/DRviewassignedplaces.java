package com.example.garbagemanagementsystem;

import androidx.appcompat.app.AppCompatActivity;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.widget.ListView;

public class DRviewassignedplaces extends AppCompatActivity {
    ListView l1;
    SharedPreferences sh;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_drviewassignedplaces);
        l1=findViewById(R.id.List1);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
    }
}