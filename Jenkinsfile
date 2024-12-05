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
                bat """
                venv\\Scripts\\activate
                pip install -r requirements.txt
                """
            }
        }
        stage('Run Application') {
            steps {
                // Start the app
                bat 'start python app.py'
                sleep(time: 5) // Ensure the app is running before tests
                
                // Run an additional Python script
                bat 'python script.py'
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