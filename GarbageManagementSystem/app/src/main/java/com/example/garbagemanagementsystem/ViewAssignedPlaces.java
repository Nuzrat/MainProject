package com.example.garbagemanagementsystem;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.util.Log;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class ViewAssignedPlaces extends AppCompatActivity {
    ListView l1;
    SharedPreferences sh;
    String url;
    ArrayList<String>Place_id,Place,Latitude,Longitude;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_assigned_places);



        url = "http://" + sh.getString("ip", "") + ":5000/Viewassingnedplaces";
        RequestQueue queue = Volley.newRequestQueue(ViewAssignedPlaces.this);
        StringRequest stringRequest = new StringRequest(Request.Method.POST, url, new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                // Display the response string.
                Log.d("+++++++++++++++++", response);
                try {

                    JSONArray ar = new JSONArray(response);

                    Place_id = new ArrayList<>();
                    Place = new ArrayList<>();
                    Latitude = new ArrayList<>();
                    Longitude = new ArrayList<>();

                    for (int i = 0; i < ar.length(); i++) {
                        JSONObject jo = ar.getJSONObject(i);
                        Place_id.add(jo.getString("Place_id"));
                        Place.add(jo.getString("Place"));
                        Latitude.add(jo.getString("Latitude"));
                        Longitude.add(jo.getString("Longitude"));


                    }

                     ArrayAdapter<String> ad=new ArrayAdapter<>(ViewAssignedPlaces.this,android.R.layout.simple_list_item_1,Place);
                    l1.setAdapter(ad);

                    // l1.setAdapter(new custom(ViewProductBook.this, title, type, details,time));
//                    l1.setOnItemClickListener(view_menu.this);

                } catch (Exception e) {
                    Log.d("=========", e.toString());
                }


            }

        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

                Toast.makeText(ViewAssignedPlaces.this, "err" + error, Toast.LENGTH_SHORT).show();
            }
        }) {
            @NonNull
            @Override
            protected Map<String, String> getParams() {
                Map<String, String> params = new HashMap<>();
//                params.put("lid", sh.getString("lid", ""));
                return params;
            }
        };
        queue.add(stringRequest);

    }
}