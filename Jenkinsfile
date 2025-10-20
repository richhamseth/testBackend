pipeline {
    agent any  // Run on any available Jenkins agent

    stages {
        stage('Checkout') {
            steps {
                // Clone the repository
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building the project...'
                sh 'echo "Simulating build step...."'
                sh '''cd app
                    docker build -t api-server:test --target run .'''
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                // Example: run unit tests
                sh 'echo "Simulating test step..."'
                sh '''cd app
                    docker build -t api-server:test --target test .
                    docker run --rm api-server:test
                    docker rmi api-server:test'''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying...'
                sh 'echo "Simulating deploy step..."'
                sh 'docker run -d -p 8085:8080 api-server:run'
                sh 'docker system prune -f'
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
