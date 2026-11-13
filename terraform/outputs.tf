output "instance_public_ip" {
  value = aws_instance.devops.public_ip
}

output "ecr_repository_url" {
  value = aws_ecr_repository.orders.repository_url
}

output "vpc_id" {
  value = aws_vpc.main.id
}