import 'package:flutter/material.dart';
import 'screens/dashboardPage.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Dashboard App',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: SplashScreen(), // Set SplashScreen as the initial screen
    );
  }
}

class SplashScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // Navigate to DashboardPage after 3 seconds
    Future.delayed(Duration(seconds: 3), () {
      Navigator.pushReplacement(
        context,
        MaterialPageRoute(builder: (context) => DashboardPage()),
      );
    });

    return Scaffold(
      backgroundColor: Colors.white, // Background color for the splash screen
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(
              "Lincoln",
              style: TextStyle(
                fontSize: 36.0,
                fontWeight: FontWeight.bold,
                color: Colors.blueAccent, // Customize color
              ),
            ),
            SizedBox(height: 10.0), // Space between the two lines
            Text(
              "(Travel Companion)",
              style: TextStyle(
                fontSize: 20.0,
                color: Colors.grey, // Customize color
              ),
            ),
          ],
        ),
      ),
    );
  }
}
