package com.company;

import java.net.HttpURLConnection;
import java.net.URL;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;

public class NewsClient {

    private static final String API_KEY = "66c2e12a4d234e33b3df8d3057ea4a5a";
    private static final String USER_AGENT = "Mozilla/5.0";
    private static final String ENDPOINT = "http://newsapi.org/v2/everything";

    public static void main(String[] args) {
        getByKeyword("facebook");
    }

    public static void getByKeyword(String keyword) {
        String url = ENDPOINT + "?from=2020-01-22&sortBy=popularity&apiKey=" + API_KEY + "&q=" + keyword;
        System.out.println(url);
    }

    private static String sendGet(String url) {
        try {
            URL obj = new URL(url);
            HttpURLConnection con = (HttpURLConnection) obj.openConnection();
            con.setRequestMethod("GET");
            con.setRequestProperty("User-Agent", USER_AGENT);
            int responseCode = con.getResponseCode();

            if (responseCode == HttpURLConnection.HTTP_OK) { // success
                BufferedReader in = new BufferedReader(new InputStreamReader(
                    con.getInputStream()));
                String inputLine;
                StringBuffer response = new StringBuffer();

                while ((inputLine = in.readLine()) != null) {
                    response.append(inputLine);
                }
                in.close();

                return response.toString();
            } else {
                System.out.println("HTTP STATUS: " + responseCode);
            }
        } catch(Exception e) {
            // nobody cares, stfu
            return "AHHHH";
        }
        return "";
    }

}
