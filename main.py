# main.py
import numpy as np
import matplotlib.pyplot as plt
from ypstruct import structure
import graph
import genaticalgorithm
from tkinter import *
from tkinter import messagebox, scrolledtext
import tkinter as tk
import backtrack
import networkx as nx
import time

global mutation_rate_entry
global population_size_entry
global num_generations
num_generations = 10
algorithm_executed = False

        
        
        
def run_genetic_algorithm():
 global algorithm_executed
 if not algorithm_executed:
    algorithm_executed = True
    # Get user inputs from entry widgets
    num_generations = 10
    mutation_rate = float(mutation_rate_entry.get())
    population_size = int(population_size_entry.get())

    adjacency_list = adjacency_list_input.get("1.0", tk.END)
    G = graph.create_graph(adjacency_list)
    
    # Record start time
    start_time_genetic = time.time()

    best_solution = genaticalgorithm.genetic_algorithm(G, population_size=population_size, mutation_rate=mutation_rate, num_generations=num_generations)

    # Calculate elapsed time
    elapsed_time_genetic = time.time() - start_time_genetic

    chromatic_number_val = genaticalgorithm.chromatic_number(best_solution)

    # Display results in a message box
    result_message = f"Genetic Algorithm Result:\nBest solution: {best_solution}\nChromatic Number: {chromatic_number_val}\nExecution Time: {elapsed_time_genetic:.4f} seconds\n\n"
    messagebox.showinfo("Genetic Algorithm Result", result_message)

    # Visualize the graph
    graph.visualize_graph(G, best_solution)


        
def run_backtrack_algorithm():
    global algorithm_executed
    if not algorithm_executed:
        algorithm_executed = True
        adjacency_list = adjacency_list_input.get("1.0", tk.END)
        G = graph.create_graph(adjacency_list)

        # Record start time
        start_time_backtrack = time.time()

        colored_graph, max_colors_needed = backtrack.create_colored_graph(G)

        # Calculate elapsed time
        elapsed_time_backtrack = time.time() - start_time_backtrack

        # Display results in a message box
        backtrack_result_message = f"Backtrack Algorithm Result:\nMinimum colors needed: {max_colors_needed}\nElapsed Time: {elapsed_time_backtrack:.4f} seconds"
        messagebox.showinfo("Backtrack Algorithm Result", backtrack_result_message)

        # Visualize the backtrack algorithm result
        pos = nx.spring_layout(colored_graph)
        node_colors = [colored_graph.nodes[node]['color'] for node in colored_graph.nodes]
        nx.draw(colored_graph, pos, with_labels=True, node_color=node_colors, cmap=plt.cm.rainbow, font_weight='bold')
        plt.show()


        
def on_button_click():
    global algorithm_executed
    if not algorithm_executed:
        algorithm_executed = True
        # This function will be called when the button is clicked
        adjacency_list = adjacency_list_input.get("1.0", tk.END)

        # Pass the adjacency list to the create_graph function in the graph module
        G = graph.create_graph(adjacency_list)

        if G is not None:
            # Run the genetic algorithm
            start_time_genetic = time.time()  # Record start time
            mutation_rate = float(mutation_rate_entry.get())
            population_size = int(population_size_entry.get())
            best_solution_genetic = genaticalgorithm.genetic_algorithm(G, population_size=population_size,
                                                                       mutation_rate=mutation_rate, num_generations=num_generations)
            elapsed_time_genetic = time.time() - start_time_genetic  # Calculate elapsed time
            chromatic_number_genetic = genaticalgorithm.chromatic_number(best_solution_genetic)
            
            # Display results in a message box
            genetic_result_message = f"Genetic Algorithm Result:\nBest solution: {best_solution_genetic}\nChromatic Number: {chromatic_number_genetic}\nElapsed Time: {elapsed_time_genetic:.6f} seconds"
            messagebox.showinfo("Genetic Algorithm Result", genetic_result_message)


            # Visualize the genetic algorithm result
            graph.visualize_graph(G, best_solution_genetic)

            # Run the backtrack algorithm
            start_time_backtrack = time.time()  # Record start time
            colored_graph, max_colors_needed = backtrack.create_colored_graph(G)
            elapsed_time_backtrack = time.time() - start_time_backtrack  # Calculate elapsed time
          
          
            # Display results in a message box
            backtrack_result_message = f"Backtrack Algorithm Result:\nMinimum colors needed: {max_colors_needed}\nElapsed Time: {elapsed_time_backtrack:.6f} seconds"
            messagebox.showinfo("Backtrack Algorithm Result", backtrack_result_message)


            # Visualize the backtrack algorithm result
            pos = nx.spring_layout(colored_graph)
            node_colors = [colored_graph.nodes[node]['color'] for node in colored_graph.nodes]
            nx.draw(colored_graph, pos, with_labels=True, node_color=node_colors, cmap=plt.cm.rainbow, font_weight='bold')
            plt.show()

            # Plot the chromatic number comparison
            plt.figure(figsize=(8, 5))
            algorithms = ['Genetic Algorithm', 'Backtrack Algorithm']
            chromatic_numbers = [chromatic_number_genetic, max_colors_needed]

            plt.bar(algorithms, chromatic_numbers, color=['green', 'red'])
            plt.xlabel('Algorithm')
            plt.ylabel('Chromatic Number')
            plt.title('Chromatic Number Comparison between Genetic and Backtrack Algorithms')
            plt.show()
            
            
            # Plot the time difference
            plt.figure(figsize=(8, 5))
            algorithms = ['Genetic Algorithm', 'Backtrack Algorithm']
            elapsed_times = [elapsed_time_genetic, elapsed_time_backtrack]

            plt.bar(algorithms, elapsed_times, color=['blue', 'orange'])
            plt.xlabel('Algorithm')
            plt.ylabel('Elapsed Time (seconds)')
            plt.title('Elapsed Time Comparison between Genetic and Backtrack Algorithms')
            plt.show()




def create_gui():
    global mutation_rate_entry
    global population_size_entry

    # Create the main window
    window = tk.Tk()
    window.title("Graph Coloring Solver")

    # Set the size of the GUI
    window.geometry("800x600")

    # Create a frame for better organization
    main_frame = Frame(window, padx=20, pady=20)
    main_frame.pack(expand=True, fill="both")

    # Create a text area for the user to input the adjacency list
    adjacency_list_label = tk.Label(main_frame, text="Enter Adjacency List:")
    adjacency_list_label.pack(pady=10)

    global adjacency_list_input
    adjacency_list_input = scrolledtext.ScrolledText(main_frame, width=40, height=10, wrap=tk.WORD, state=tk.NORMAL)
    adjacency_list_input.pack(pady=10)

    # Create entry widgets for mutation_rate, population_size, and num_generations
    mutation_rate_label = tk.Label(main_frame, text="Mutation Rate:")
    mutation_rate_label.pack(pady=5)
    mutation_rate_entry = tk.Entry(main_frame)
    mutation_rate_entry.pack(pady=5)

    population_size_label = tk.Label(main_frame, text="Population Size:")
    population_size_label.pack(pady=5)
    population_size_entry = tk.Entry(main_frame)
    population_size_entry.pack(pady=5)

    # Create a button that runs both algorithms
    button_both = tk.Button(main_frame, text="Run Both Algorithms", command=on_button_click)
    button_both.pack(pady=10)

    # Create a button that runs the genetic algorithm
    button_genetic = tk.Button(main_frame, text="Run Genetic Algorithm", command=run_genetic_algorithm)
    button_genetic.pack(pady=10)

    # Create a button that runs the backtrack algorithm
    button_backtrack = tk.Button(main_frame, text="Run Backtrack Algorithm", command=run_backtrack_algorithm)
    button_backtrack.pack(pady=10)

    # Run the GUI
    window.mainloop()


# Call the function to create the GUI
create_gui()
