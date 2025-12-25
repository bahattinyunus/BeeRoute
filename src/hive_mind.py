"""
BeeRoute: Kovan Zihni Çekirdeği
===============================
BeeRoute mimarisinin merkezi komuta düğümü.
Gezgin Satıcı Problemini çözen ajan sürüsünü simüle eder.

Mimar: Bahattin Yunus Çetin (IT Architect)
Lokasyon: Trabzon / Of
Web: https://github.com/bahattinyunus
"""

import time
import random
import sys
import threading
from colorama import init, Fore, Style
from src.pheromone_matrix import PheromoneMatrix

# Initialize colorama
init(autoreset=True)

class HiveMind:
    def __init__(self, node_count=10, colony_size=20):
        self.node_count = node_count
        self.colony_size = colony_size
        self.matrix = PheromoneMatrix(node_count)
        self.best_global_route = None
        self.best_global_score = float('inf')
        self.lock = threading.Lock()

    def log(self, level, message):
        if level == "INFO":
            print(f"{Fore.CYAN}[KOVAN_BİLGİ]{Style.RESET_ALL} {message}")
        elif level == "SUCCESS":
            print(f"{Fore.GREEN}[BAŞARILI]{Style.RESET_ALL} {message}")
        elif level == "WARN":
            print(f"{Fore.YELLOW}[UYARI]{Style.RESET_ALL} {message}")
        elif level == "CRITICAL":
            print(f"{Fore.RED}[KRİTİK]{Style.RESET_ALL} {message}")

    def _simulate_bee(self, bee_id):
        # ... (same logic) ...
        current_node = 0
        unvisited = list(range(1, self.node_count))
        path = [0]
        distance = 0
        
        while unvisited:
            # Choose next node based on pheromones (roulette wheel selection)
            weights = self.matrix.get_probability_weights(current_node, unvisited)
            next_node = random.choices(unvisited, weights=weights, k=1)[0]
            
            # Simulated distance
            dist = random.uniform(1.0, 10.0)
            
            path.append(next_node)
            distance += dist
            unvisited.remove(next_node)
            current_node = next_node
            
            # Tiny sleep to visualize "work"
            time.sleep(random.uniform(0.01, 0.05))

        # Return to hive
        path.append(0)
        
        with self.lock:
            if distance < self.best_global_score:
                self.best_global_score = distance
                self.best_global_route = path
                self.log("SUCCESS", f"Arı #{bee_id} yeni optimum yol keşfetti! Mesafe: {distance:.2f}")
                # Reinforce this good path
                self.matrix.deposit(path, amount=10.0/distance)

    def run_simulation(self, generations=5, visualize=False):
        self.log("INFO", f"Trabzon Protokolü Başlatılıyor... Düğümler: {self.node_count}, Ajanlar: {self.colony_size}")
        time.sleep(1)
        self.log("INFO", "Feromon Matrisi: ÇEVRİMİÇİ")
        time.sleep(0.5)
        
        for generation in range(1, generations + 1):
            print(f"\n{Fore.MAGENTA}--- NESİL {generation} ---{Style.RESET_ALL}")
            threads = []
            for i in range(self.colony_size):
                t = threading.Thread(target=self._simulate_bee, args=(i,))
                threads.append(t)
                t.start()
            
            for t in threads:
                t.join()
            
            # Global evaporation
            self.matrix.decay()
            self.log("INFO", f"Nesil {generation} tamamlandı. Küresel Feromonlar güncellendi.")

        print(f"\n{Fore.GREEN}=========================================={Style.RESET_ALL}")
        print(f"{Fore.GREEN}OPTİMİZASYON TAMAMLANDI{Style.RESET_ALL}")
        print(f"En İyi Rota: {self.best_global_route}")
        print(f"Toplam Mesafe: {self.best_global_score:.2f}")
        print(f"{Fore.GREEN}=========================================={Style.RESET_ALL}")

        if visualize and self.best_global_route:
            try:
                from src.visualizer import HiveVisualizer
                viz = HiveVisualizer(self.node_count)
                viz.plot_route(self.best_global_route, self.best_global_score)
                self.log("SUCCESS", "Görsel rapor oluşturuldu: route_result.png")
            except ImportError as e:
                self.log("WARN", f"Görselleştirme hatası: {e}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="BeeRoute: Trabzon Protocol Simulation")
    parser.add_argument("--nodes", type=int, default=10, help="Number of nodes (cities) in the graph")
    parser.add_argument("--bees", type=int, default=20, help="Number of forager bees")
    parser.add_argument("--gens", type=int, default=5, help="Number of generations")
    parser.add_argument("--visualize", action="store_true", help="Generate a visual graph of the route")
    
    args = parser.parse_args()
    
    hive = HiveMind(node_count=args.nodes, colony_size=args.bees)
    hive.run_simulation(generations=args.gens, visualize=args.visualize)
