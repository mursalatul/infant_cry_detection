# Infant Cry Detection System

An intelligent web application designed to analyze and classify infant cries to help parents and caregivers better understand their baby's needs. This project uses machine learning to detect and classify different types of infant cries, providing valuable insights into the baby's discomfort levels and potential reasons for crying.

## Features

### 1. Main Pages
- **Home Page**: Landing page with overview of the system
- **Cry Detection**: Core feature for analyzing infant cries
- **Discomfort Analysis**: Detailed analysis of baby's discomfort levels
- **Tutorial**: Guide on how to use the system
- **About**: Information about the project and team
- **Results**: Display analysis results

### 2. Key Features
- Real-time audio recording and analysis
- Machine learning-based cry classification
- Discomfort level assessment
- Historical data tracking
- Responsive web design
- User-friendly interface

## Technology Stack

### Backend
- **Django**: High-level Python web framework
  - Chosen for its robust security features and rapid development capabilities
  - Built-in admin interface
  - Excellent ORM for database operations

### Machine Learning
- **scikit-learn**: For implementing machine learning models
- **librosa**: For audio signal processing
- **numpy**: For numerical computations
- **scipy**: For scientific computations

### Frontend
- **Bootstrap**: For responsive and modern UI design
- **crispy-forms**: For enhanced form rendering
- **HTML/CSS/JavaScript**: For frontend implementation

### Database
- **SQLite**: For development
- Support for PostgreSQL in production

### Audio Processing
- **pydub**: For audio file manipulation
- **soundfile**: For reading and writing audio files
- **audioread**: For cross-platform audio file reading

## Project Structure
```
├── about/                 # About page application
├── cry_detection/         # Core cry detection functionality
├── discomfort/           # Discomfort analysis module
├── index/                # Home page application
├── result/               # Results display module
├── tutorial/             # Tutorial page application
├── media/                # User uploaded files
├── static/               # Static files (CSS, JS, Images)
└── templates/            # Base templates
```

## Features in Detail

1. **Cry Detection Module**
   - Real-time audio recording
   - ML model integration for cry analysis
   - Result visualization

2. **Discomfort Analysis**
   - Detailed analysis of crying patterns
   - Discomfort level assessment
   - Historical data tracking

3. **Tutorial System**
   - Step-by-step guidance
   - Best practices for recording
   - Usage instructions

4. **Results Dashboard**
   - Detailed analysis results
   - Historical data view
   - Export functionality

## Installation

1. Clone the repository:
```bash
git clone https://github.com/mursalatul/infant_cry_detection.git
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Add your license information here]

## Authors

- Mursalatul Islam
