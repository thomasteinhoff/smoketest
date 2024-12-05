pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Run Application') {
            steps {
                bat 'python app.py'
            }
        }
        stage('Run Smoke Tests') {
            steps {
                bat 'pytest test_smoke.py'
            }
        }
        stage('Check Python') {
            steps {
                bat 'python --version'
                bat 'pip --version'
            }
        }   
    }

    post {
        always {
            echo 'Cleaning up...'
            bat 'taskkill /F /IM python.exe || exit 0'
        }
    }
}