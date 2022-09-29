package com.example.taskmap;

import java.net.*;
import java.io.*;

public class Client {
    private Socket clientSocket;

    private OutputStream out;
    private DataInputStream in;

    public void startConnection(String ip, int port) throws IOException {
        clientSocket = new Socket(ip, port);
        out = clientSocket.getOutputStream();
        in = new DataInputStream(clientSocket.getInputStream());
    }

    public void sendMessage(byte[] msg) throws IOException {
        out.write(msg);
    }

    public byte[] receiveMessage() throws IOException {
        int length = in.available();

        System.out.println(length);

        while (length == 0){
            length = in.available();
        }

        System.out.println(length);

        byte[] massageByte = new byte[length];
        in.read(massageByte);
        return massageByte;

    }


    public void stopConnection() throws IOException {
        in.close();
        out.close();
        clientSocket.close();
    }
}