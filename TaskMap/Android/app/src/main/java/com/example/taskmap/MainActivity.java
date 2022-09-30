package com.example.taskmap;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import java.io.IOException;
import java.nio.charset.StandardCharsets;

public class MainActivity extends AppCompatActivity {

    private EditText TextView;
    private Button btn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        TextView = findViewById(R.id.Text);
        btn      = findViewById(R.id.btn);


        Client client = new Client();
            new Thread(new Runnable() {
                public void run() {
                    try {
                        client.startConnection("192.168.0.104", 8000);
                        client.sendMessage("admin".getBytes());

                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
            }).start();

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String text = TextView.getText().toString();
                new Thread(new Runnable() {
                    public void run() {
                        try {
                            client.sendMessage(text.getBytes(StandardCharsets.UTF_8));
                        } catch (IOException e) {
                            e.printStackTrace();
                        }
                    }
                }).start();
            }
        });
    }
}