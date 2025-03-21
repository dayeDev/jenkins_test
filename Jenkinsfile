pipeline {
    agent any
    
    // 가상환경 안씀
    // environment {
    //     VENV_DIR = "${WORKSPACE}/venv"
    // }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/kimjeongjae1/0319TeamRepo.git'
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    pytest
                '''
            }
        }
    }

    post {
        always {
            echo 'Build finished.'
        }
    }
}