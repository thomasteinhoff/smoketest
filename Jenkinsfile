pipeline {
    agent {
        docker { image 'python:3.9-slim' }  // Use the Python image
    }
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Application') {
            steps {
                sh 'python your_application.py'
            }
        }
    }
}
