# celery-beat-task-scheduler
Scheduling task (work order) using celery 

# Celery

1. Task Queue Framework:

    Purpose: Celery is a distributed task queue system that enables you to run asynchronous tasks and schedule them to run at a later time.

    Functionality: It allows you to define tasks in your code and execute them asynchronously, distribute them across multiple worker nodes, and manage task execution.

2. Components:

    Tasks: Functions or methods defined in your code that are executed asynchronously by Celery workers.

    Workers: Processes that run the tasks. They listen for tasks on a message broker (such as RabbitMQ or Redis) and execute them.

    Brokers: Middleware (e.g., RabbitMQ, Redis) that facilitates communication between the application (task producers) and the Celery workers (task consumers).

# Celery Beat

1. Scheduler:

    Purpose: Celery Beat is a scheduler that enables you to schedule periodic tasks (tasks that need to be run at regular intervals).
    Functionality: It works alongside Celery to schedule tasks at specific intervals (e.g., every hour, daily, etc.). Celery Beat uses the Celery worker to execute these scheduled tasks.

2. Components:

Scheduler: Celery Beat itself, which periodically sends tasks to the Celery workers based on the defined schedule.
Schedule Storage: A place to store the schedule. This can be in-memory, in a database, or another backend supported by Celery.


# Conclusion

In summary, Celery is the core component that allows you to run and manage asynchronous tasks, while Celery Beat extends Celery's functionality by adding the ability to schedule tasks to run at regular intervals. Both components are often used together in applications that require both asynchronous task execution and periodic task scheduling.