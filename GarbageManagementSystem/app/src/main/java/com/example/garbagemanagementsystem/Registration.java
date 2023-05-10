package com.example.garbagemanagementsystem;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class Registration extends AppCompatActivity {
    EditText e1,e2,e3,e4,e5,e6,e7,e8,e9;
    Button b1;
    SharedPreferences sh;
    String fname,lname,place,post,pin,phone,email,username,password;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_registration);
        e1=findViewById(R.id.editTextTextPersonName5);
        e2=findViewById(R.id.editTextTextPersonName6);
        e3=findViewById(R.id.editTextTextPersonName7);
        e4=findViewById(R.id.editTextTextPersonName8);
        e5=findViewById(R.id.editTextTextPersonName9);
        e6=findViewById(R.id.editTextTextPersonName10);
        e7=findViewById(R.id.editTextTextPersonName11);
        e8=findViewById(R.id.editTextTextPersonName12);
        e9=findViewById(R.id.editTextTextPersonName13);
        b1=findViewById(R.id.button16);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                fname=e1.getText().toString();
                lname=e2.getText().toString();
                place=e3.getText().toString();
                post=e4.getText().toString();
                pin=e5.getText().toString();
                phone=e6.getText().toString();
                email=e7.getText().toString();
                username=e8.getText().toString();
                password=e9.getText().toString();

                RequestQueue queue = Volley.newRequestQueue(Registration.this);
                String url = "http://" + sh.getString("ip", "") + ":5000/userreg";

                // Request a string response from the provided URL.
                StringRequest stringRequest = new StringRequest(Request.Method.POST, url, new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        // Display the response string.
                        Log.d("+++++++++++++++++", response);
                        try {
                            JSONObject json = new JSONObject(response);
                            String res = json.getString("task");

                            if (res.equalsIgnoreCase("success")) {
//                                String lid = json.getString("id");
//                                SharedPreferences.Editor edp = sh.edit();
//                                edp.putString("lid", lid);
//                                edp.commit();
                                Intent ik = new Intent(getApplicationContext(), login.class);
                                startActivity(ik);

                            } else {

                                Toast.makeText(Registration.this, "Invalid username or password", Toast.LENGTH_SHORT).show();

                            }
                        } catch (JSONException e) {
                            e.printStackTrace();
                        }


                    }
                }, new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {


                        Toast.makeText(getApplicationContext(), "Error" + error, Toast.LENGTH_LONG).show();
                    }
                }) {
                    @Override
                    protected Map<String, String> getParams() {
                        Map<String, String> params = new HashMap<String, String>();
                        params.put("fname",fname);
                        params.put("lname",lname);
                        params.put("place",place);
                        params.put("post",post);
                        params.put("pin",pin);
                        params.put("phone",phone);
                        params.put("email",email);
                        params.put("username", username);
                        params.put("password", password);

                        return params;
                    }
                };
                queue.add(stringRequest);

            }
        });

    }
}