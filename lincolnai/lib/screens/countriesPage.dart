import 'package:flutter/material.dart';
import 'infoPage.dart'; // Import InfoPage for navigation

class CountriesPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(
          'Countries',
          style: TextStyle(fontWeight: FontWeight.bold),
        ),
        backgroundColor: Colors.blueAccent,
        elevation: 0,
      ),
      body: Container(
        color: Colors.blueAccent.shade100.withOpacity(0.1),
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Hero Section
            Text(
              'Choose Your Destination',
              style: TextStyle(
                fontSize: 28,
                fontWeight: FontWeight.bold,
              ),
            ),
            SizedBox(height: 8),
            Text(
              'Explore immigration details for each country.',
              style: TextStyle(
                fontSize: 16,
                color: Colors.grey.shade700,
              ),
            ),
            SizedBox(height: 16),

            // Countries Grid
            Expanded(
              child: GridView.count(
                crossAxisCount: 2, // 2 columns for a modern card layout
                crossAxisSpacing: 16.0,
                mainAxisSpacing: 16.0,
                children: [
                  // United Kingdom Card
                  CountryCard(
                    countryName: 'United Kingdom',
                    flagUrl:
                    'https://upload.wikimedia.org/wikipedia/en/a/ae/Flag_of_the_United_Kingdom.svg',
                    description: 'Details about UK immigration policies.',
                    onTap: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(
                          builder: (context) => InfoPage(country: 'United Kingdom'),
                        ),
                      );
                    },
                  ),
                  // United States Card
                  CountryCard(
                    countryName: 'United States',
                    flagUrl:
                    'https://upload.wikimedia.org/wikipedia/en/a/a4/Flag_of_the_United_States.svg',
                    description: 'Explore US visa and immigration options.',
                    onTap: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(
                          builder: (context) => InfoPage(country: 'United States'),
                        ),
                      );
                    },
                  ),
                  // Canada Card
                  CountryCard(
                    countryName: 'Canada',
                    flagUrl:
                    'https://upload.wikimedia.org/wikipedia/commons/c/cf/Flag_of_Canada.svg',
                    description: 'Learn about Canadian immigration pathways.',
                    onTap: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(
                          builder: (context) => InfoPage(country: 'Canada'),
                        ),
                      );
                    },
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class CountryCard extends StatelessWidget {
  final String countryName;
  final String flagUrl;
  final String description;
  final VoidCallback onTap;

  const CountryCard({
    required this.countryName,
    required this.flagUrl,
    required this.description,
    required this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: onTap,
      child: Card(
        elevation: 4,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(16),
        ),
        child: Container(
          decoration: BoxDecoration(
            gradient: LinearGradient(
              colors: [Colors.white, Colors.blue.shade50],
              begin: Alignment.topLeft,
              end: Alignment.bottomRight,
            ),
            borderRadius: BorderRadius.circular(16),
          ),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              // Country Flag
              Container(
                width: 60,
                height: 40,
                decoration: BoxDecoration(
                  image: DecorationImage(
                    image: NetworkImage(flagUrl),
                    fit: BoxFit.cover,
                  ),
                  borderRadius: BorderRadius.circular(8),
                ),
              ),
              SizedBox(height: 12),
              // Country Name
              Text(
                countryName,
                style: TextStyle(
                  fontSize: 18,
                  fontWeight: FontWeight.bold,
                ),
                textAlign: TextAlign.center,
              ),
              SizedBox(height: 8),
              // Description
              Text(
                description,
                style: TextStyle(
                  fontSize: 14,
                  color: Colors.grey.shade600,
                ),
                textAlign: TextAlign.center,
              ),
              SizedBox(height: 8),
              // Navigate Icon
              Icon(
                Icons.arrow_forward,
                color: Colors.blueAccent,
              ),
            ],
          ),
        ),
      ),
    );
  }
}
