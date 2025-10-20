pipeline {
    agent any  // Run on any available Jenkins agent

    stages {
        // stage('Checkout') {
        //     steps {
        //         // Clone the repository
        //         checkout scm
        //     }
        // }

        stage('Build') {
            steps {
                echo 'Building the project...'
                // Example: compile or install dependencies
                sh 'echo "Simulating build step..."'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                // Example: run unit tests
                sh 'echo "Simulating test step..."'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying...'
                // Optional for testing
                sh 'echo "Simulating deploy step..."'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished!'
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
