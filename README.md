# EN - Two-Dimensional Cellular Automaton

## Project Description

This project implements a two-dimensional cellular automaton with a von Neumann neighborhood. The automaton models the behavior of cells based on their state and the state of their nearest neighbors. Toroidal boundary conditions are applied to ensure seamless grid wrapping. Users can specify the grid width and the number of iterations for simulation. Additionally, initial conditions can be set manually or generated randomly. The application interface is built using PyQT6.

## Project structure

```commandline
.
|   main.py
|   README.md
|   requirements.txt
|
+---automata
|   |   automatagrid.py
|   \   constant.py
|
+---ui
    |   choosewindow.py
    \   uigrid.py
```

## Main Components

- **`Cell` and `AutomataGrid` Classes**:  
  The `Cell` class is a simple wrapper that manages the state of an individual cell in the cellular automaton. The cell state is represented as a boolean value, where `True` or `False` indicate active or inactive states, respectively. The class provides methods for initializing and updating the cell's state.  

  The `AutomataGrid` class serves as the primary structure for managing the automaton's state using a von Neumann neighborhood. It initializes the grid of cells, provides methods for random generation of initial conditions, and computes the next iteration of the automaton. The class ensures proper handling of boundary conditions for consistent behavior at the grid edges.

- **UI Classes**:  
  - **`ChooseWindow`**:  
    This class, based on QWidget, implements the initial parameter selection window for the automaton. It allows users to input the number of rows, columns, and iterations for the simulation. A confirmation button generates and displays a new automaton grid with the specified parameters.

  - **`UIGrid`**:  
    This class, also based on QWidget, displays and manages the cellular automaton grid. Users can interact with the grid by toggling cell states through button clicks. The interface includes controls for generating initial conditions (manually or randomly), clearing the grid, and computing subsequent iterations. Additionally, it provides a slider to navigate through different simulation stages.

## Installation and Execution

1. Clone the project repository from GitHub.
   ```commandline
   git clone https://github.com/StanleyStanMarsh/cellular-automaton.git
   cd cellular-automaton
   ```

2. Install the required Python packages listed in the `requirements.txt` file.
   ```commandline
   pip install -r requirements.txt
   ```

3. Execute the main script to launch the application.
   ```commandline
   python main.py
   ```

## Configuration

- **Initial Conditions**:  
  Users can either manually configure the initial grid state or generate random conditions.

## License

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

This project is licensed under the **BSD-3-Clause License**. You are free to use, modify, and distribute this software in compliance with the license terms. See the [LICENSE](LICENSE) file for detailed information.


# RU - Two-Dimensional Cellular Automaton

## Описание проекта

Данный проект представляет собой реализацию двумерного клеточного автомата с окрестностью фон Неймана. Автомат позволяет моделировать поведение клеток в зависимости от их состояния и состояния ближайших соседей. Граничные условия в данном автомате решаются через тороидальное устройство, а пользователь может задать ширину поля и количество итераций для моделирования. Также предусмотрена возможность выбора начальных условий как вручную, так и случайным образом. Интерфейс приложения реализован на базе PyQT6.

## Структура проекта

```commandline
.
|   main.py
|   README.md
|   requirements.txt
|
+---automata
|   |   automatagrid.py
|   \   constant.py
|
+---ui
    |   choosewindow.py
    \   uigrid.py
```

### Основные компоненты

- **main.py**: Главный модуль для запуска приложения.
- **automata/**: Папка, содержащая вычислительную логику автомата.
  - **automatagrid.py**: Модуль, реализующий класс AutomataGrid, который отвечает за хранение и вычисление сетки клеточного автомата.
  - **constant.py**: Модуль для хранения констант, используемых для вычисления состояний автомата.
- **ui/**: Папка, содержащая интерфейсную часть на базе PyQT6.
  - **choosewindow.py**: Модуль для отображения окна начального выбора параметров автомата.
  - **uigrid.py**: Модуль для отрисовки и управления сеткой автомата.

### Классы Cell и AutomataGrid

`Cell` является простым классом-оберткой, который управляет состоянием отдельной клетки в клеточном автомате. Состояние клетки представляется булевым значением, где True или False указывают на активное или неактивное состояние соответственно. Класс предоставляет методы для инициализации состояния и его обновления.

`AutomataGrid` представляет собой основную структуру для управления состоянием клеточного автомата с окрестностью фон Неймана. Класс отвечает за создание и инициализацию сетки ячеек, предоставляя методы для случайной генерации начальных состояний и вычисления следующей итерации клеточного автомата. Методы класса учитывают различные граничные условия, обеспечивая корректное поведение клеток на краях сетки.

### Классы интерфейса

`ChooseWindow` — это класс пользовательского интерфейса, основанный на QWidget и реализующий окно для начального выбора параметров клеточного автомата. Он предоставляет пользователю возможность ввести количество строк, столбцов и число итераций для состояний автомата. Класс также содержит кнопку подтверждения, которая при нажатии создает и отображает новую сетку автоматов с заданными параметрами.

`UIGrid` — это класс пользовательского интерфейса на основе QWidget, который отображает и управляет сеткой клеточного автомата. Пользователи могут взаимодействовать с клетками сетки, устанавливая их состояния через нажатия кнопок. Интерфейс предоставляет элементы управления для генерации первоначальных условий (вручную или случайно), очистки сетки и расчета следующих итераций. Класс также включает элементы управления для работы с слайдером, чтобы просматривать состояние сетки на разных этапах моделирования.

## Установка и запуск

1. Клонируйте репозиторий:

   ```commandline
   git clone https://github.com/StanleyStanMarsh/cellular-automaton.git
   cd cellular-automaton
   ```

2. Установите необходимые зависимости:

   ```commandline
   pip install -r requirements.txt
   ```

3. Запустите приложение:

   ```commandline
   python main.py
   ```

## Конфигурация

- Начальные условия: Возможность ввода начальных условий вручную или их случайное задание.

## Лицензия

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

Данный проект лицензирован в соответствии с **Лицензией BSD-3-Clause**. Вы можете свободно использовать, изменять и распространять это программное обеспечение в соответствии с условиями лицензии. Подробную информацию смотрите в файле [LICENSE](LICENSE).
