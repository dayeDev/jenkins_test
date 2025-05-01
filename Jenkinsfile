pipeline {
    agent any  // 어떤 에이전트에서도 실행

    stages {
        stage('Checkout') {
            steps {
                // GitHub에서 코드 클론
                git branch: 'main', credentialsId: 'git', url: 'https://github.com/dayeDev/jenkins_test.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // pip 경로가 인식 안될 수 있으니 명시적으로 지정
                sh '''
                    export PATH="/usr/bin:$PATH"
                    /usr/bin/pip3 install --upgrade pip
                    /usr/bin/pip3 install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                // 테스트 실행 시 XML 리포트 생성
                sh '''
                    export PATH="/usr/bin:$PATH"
                    mkdir -p reports  # XML 결과 파일 저장 디렉토리
                    /usr/bin/python3 -m pytest tests --junitxml=reports/results.xml
                '''
            }
        }
    }

    post {
        always {
            // 테스트가 성공/실패와 상관없이 결과 리포트를 수집
            junit 'reports/results.xml'
        }
    }
}
