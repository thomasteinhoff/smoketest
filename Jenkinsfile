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
                sh 'pip install flask requests pytest'
            }
        }
        stage('Run Application') {
            steps {
                sh 'nohup python app.py &'
                sleep(time: 5) // Ensure the app is running before tests
            }
        }
        stage('Run Smoke Tests') {
            steps {
                sh 'pytest test_smoke.py'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            sh 'pkill -f app.py || true'
        }
    }
}
