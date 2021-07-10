pipeline {
  environment {
    imagename = "jakubbialoskorski/notty"
    registryCredential = 'dockerhub_id'
    dockerImage = ''
  }
  agent any
  stages {
    stage('Cloning GitHub repository') {
      steps {
        git([url: 'https://github.com/JakubBialoskorski/notty.git', branch: 'master', credentialsId: 'github_readonly'])
      }
    }
    stage('Building docker image') {
      steps{
        script {
          dockerImage = docker.build imagename
        }
      }
    }
    stage('Running unit tests') {
      steps{
        script {
          sh 'docker run -d -p 80:80 --name notty jakubbialoskorski/notty'
          sh 'docker exec notty python -m unittest discover'
          echo 'TESTS PASSED'
          sh 'docker stop notty && docker rm notty'
        }
      }
    }
    stage('Pushing docker image') {
      steps{
        script {
          docker.withRegistry( '', registryCredential ) {
             dockerImage.push('latest')
          }
        }
      }
    }
    stage('Cleaning up docker image') {
      steps{
         sh "docker rmi -f $imagename:latest"
      }
    }
  }
}