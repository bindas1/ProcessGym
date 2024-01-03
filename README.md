# Deep Reinforcement Learning for Resource Allocation in Business Processes

## Project Overview

This repository presents an in-depth assessment and analysis of "Deep Reinforcement Learning for Resource Allocation in Business Processes." The primary focus is on evaluating the performance of Deep Q-Network (DQN) learning in comparison to traditional algorithms like First In, First Out (FIFO) and Shortest Processing Time (SPT).

## Getting Started

1. Set up the environment with Python 3.8 (recommended to use conda).

```conda create --name process_gym python=3.8```

2. Activate the environment

```conda activate process_gym```

3. Install the dependencies:

```pip install -r requirements.txt```

### Baseline Results

To obtain baseline results, run the notebook `Process_gym_spt-fifo.ipynb`. Note that executing the cells for FIFO and SPT algorithms (30 times) may take at least two hours. The notebook also compares results for recreation and extension, saved in `results_recreation_3000` and `results_extension_3000` folders.

### DQN Learning Results

To obtain DQN learning results:

1. To get single results for recreation / extension run either:
- `python dqn_learning.py recreation`
- `python dqn_learning.py extension`

2. If you want to run both algorithms 30 times you can just use `script.sh` that I implemented but note that each run will take approximately 2 hours to complete so the whole script will take 120 hours on a single core...

To evaluate the results and create charts for the obtained models run `dqn_learning.ipynb`. I have already provided the results that I obtained in the corresponding folder and running this notebook with the prepared files should take almost no time.

<!-- ABOUT THE PROJECT -->
## About The Project
For the purpose of using tabular and approximate algorithms in the area of reinforcement learning, we designed and developed a dedicated simulation environment that we call ProcessGym.
It can serve as a general-purpose framework for testing resource allocation algorithms.

## Configuration files JSON schemas
Examples of config files are in **conf** directory.

### Simulation config
```json
{
  "title": "Simulation config",
  "type": "object",
  "properties": {
    "process_case_probability": {
      "description": "Probability of new process case arriving in each step",
      "type": "number"
    },
    "queue_capacity_modifier": {
      "description": "Modifier limiting size of enabled_tasks queue",
      "type": "number"
    },
    "available_resources": {
      "description": "List of available resources",
      "type": "array",
      "items": {
        "type": "number"
      },
      "loaded_processes": {
        "description": "List of processes definitions to be loaded",
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "filename": {
              "description": "Path to process definition file",
              "type": "string"
            },
            "frequency": {
              "description": "Relative frequency of process case appearance",
              "type": "number"
            },
            "reward": {
              "description": "Reward for completing process case",
              "type": "number"
            }
          }
        }
      }
    }
  }
}
```
### Process definition schema
```json
{
  "title": "Process definition",
  "type": "object",
  "properties": {
    "process_id": {
      "description": "Unique identifier of business process",
      "type": "number"
    },
    "tasks": {
      "description": "List of tasks",
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "description": "Unique task identifier",
            "type": "number"
          },
          "duration": {
            "description": "Average task duration",
            "type": "number"
          },
          "duration_sd": {
            "description": "Standard deviation of task duration",
            "type": "number"
          },
          "start": {
            "description": "Flag indicating whether business process starts with this task",
            "type": "boolean"
          },
          "transitions": {
            "description": "List of possible task transitions",
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "id": {
                  "description": "Task identfier",
                  "type": "number"
                },
                "probability": {
                  "description": "Probability of transitioning to task",
                  "type": "number"
                }
              }
            }
          }
        }
      }
    }
  }
}
```

### Resource eligibility config
```json
{
  "title": "Resource eligibilities",
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "resource_eligibility": {
        "description": "List of eligible resources for tasks",
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "task_id": {
              "description": "Task identifier",
              "type": "number"
            },
            "eligible_resources": {
              "type": "object",
              "properties": {
                "_resource_id": {
                  "description": "Task duration modifier (_resource_id must be a number)",
                  "type": "number"
                }
              }
            }
          }
        }
      }
    }
  }
}
```





<!-- CONTRIBUTING -->
## Contributing

Any contributions you make are appreciated.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/NewFeature`)
3. Commit your Changes (`git commit -m 'Add some NewFeature'`)
4. Push to the Branch (`git push origin feature/NewFeature`)
5. Open a Pull Request



[comment]: <> (<!-- LICENSE -->)

[comment]: <> (## License)

[comment]: <> (Distributed under the MIT License. See `LICENSE` for more information.)


