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
                bat 'pip install flask requests pytest'
            }
        }
        stage('Run Application') {
            steps {
                bat 'nohup python app.py &'
                sleep(time: 5) // Ensure the app is running before tests
            }
        }
        stage('Run Smoke Tests') {
            steps {
                bat 'pytest test_smoke.py'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            bat 'pkill -f app.py || true'
        }
    }
}
