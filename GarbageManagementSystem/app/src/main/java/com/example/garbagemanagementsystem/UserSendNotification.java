package com.example.garbagemanagementsystem;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.app.DatePickerDialog;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.DatePicker;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONObject;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.HashMap;
import java.util.Locale;
import java.util.Map;

public class UserSendNotification extends AppCompatActivity {
    EditText e1;
    Spinner s1;
    Button b1;
    SharedPreferences sh;
    String notification,url;
    ArrayList<String>fname,lname,lid;
    final Calendar myCalendar= Calendar.getInstance();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_user_send_notification);
        e1=findViewById(R.id.editTextTextPersonName15);
        s1=findViewById(R.id.spinner2);
        b1=findViewById(R.id.button17);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

        DatePickerDialog.OnDateSetListener date =new DatePickerDialog.OnDateSetListener() {
            @Override
            public void onDateSet(DatePicker view, int year, int month, int day) {
                myCalendar.set(Calendar.YEAR, year);
                myCalendar.set(Calendar.MONTH,month);
                myCalendar.set(Calendar.DAY_OF_MONTH,day);
                updateLabel();
            }
        };
        e1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                new DatePickerDialog(UserSendNotification.this,date,myCalendar.get(Calendar.YEAR),myCalendar.get(Calendar.MONTH),myCalendar.get(Calendar.DAY_OF_MONTH)).show();
            }
        });

        url = "http://" + sh.getString("ip", "") + ":5000/viewdriver";
        RequestQueue queue = Volley.newRequestQueue(UserSendNotification.this);
        StringRequest stringRequest = new StringRequest(Request.Method.POST, url, new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                // Display the response string.
                Log.d("+++++++++++++++++", response);
                try {

                    JSONArray ar = new JSONArray(response);

                    fname = new ArrayList<>();

                    lid = new ArrayList<>();

                    for (int i = 0; i < ar.length(); i++) {
                        JSONObject jo = ar.getJSONObject(i);
                        fname.add(jo.getString("F_name")+jo.getString("L_name"));

                        lid.add(jo.getString("login_id"));


                    }

                     ArrayAdapter<String> ad=new ArrayAdapter<>(UserSendNotification.this,android.R.layout.simple_list_item_1,fname);
                    s1.setAdapter(ad);

//                    l1.setAdapter(new custom2(UserSendNotification.this, fname,lname));
//                    l1.setOnItemClickListener(view_menu.this);

                } catch (Exception e) {
                    Log.d("=========", e.toString());
                }


            }

        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

                Toast.makeText(UserSendNotification.this, "err" + error, Toast.LENGTH_SHORT).show();
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



        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                notification=e1.getText().toString();

            }
        });

    }

    private void updateLabel(){
        String myFormat="MM/dd/yy";
        SimpleDateFormat dateFormat=new SimpleDateFormat(myFormat, Locale.US);
        e1.setText(dateFormat.format(myCalendar.getTime()));
    }

}