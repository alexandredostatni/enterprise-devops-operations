variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-2"
}

variable "project_name" {
  description = "Project name"
  type        = string
  default     = "techcorp-devops"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.large"
}

variable "ssh_cidr" {
  description = "Allowed SSH source CIDR"
  type        = string
}

variable "github_repository" {
  description = "GitHub repository allowed to assume the publishing role"
  type        = string
  default     = "alexandredostatni/enterprise-devops-operations"
}