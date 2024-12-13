with open("Input Files/inputTest","r") as f:
    lines = f.readlines()

class Coords:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Coords(X={self.x}, Y={self.y})"


def firstGoldStar(lines):
    count = 0
    button_a = Coords()
    button_b = Coords()
    prizes = Coords()

    for line in lines:
        if "Button A" in line:
            parts = line.strip().split(", ")
            x_value = int(parts[0].split("+")[1])
            y_value = int(parts[1].split("+")[1])
            button_a.__init__(x_value, y_value)
        elif "Button B" in line:
            parts = line.strip().split(", ")
            x_value = int(parts[0].split("+")[1])
            y_value = int(parts[1].split("+")[1])
            button_b.__init__(x_value, y_value)
        elif "Prize" in line:
            parts = line.strip().split(", ")
            x_value = int(parts[0].split("=")[1])
            y_value = int(parts[1].split("=")[1])
            prizes.__init__(x_value, y_value)
        else:
            min_cost = float('inf')
            for a_count in range(prizes.x // button_a.x + 1):
                remaining_x_coords = prizes.x - a_count * button_a.x
                if remaining_x_coords % button_b.x == 0:
                    b_count = remaining_x_coords // button_b.x
                    if a_count * button_a.y + b_count * button_b.y == prizes.y and a_count <= 100 and b_count <= 100:
                        min_cost = min(min_cost, a_count * 3 + b_count * 1)
            if min_cost != float("inf"): count += min_cost

    return count

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

def secondGoldStar(lines):
    count = 0
    button_a = Coords()
    button_b = Coords()
    prizes = Coords()

    for line in lines:
        if "Button A" in line:
            parts = line.strip().split(", ")
            x_value = int(parts[0].split("+")[1])
            y_value = int(parts[1].split("+")[1])
            button_a.__init__(x_value, y_value)
        elif "Button B" in line:
            parts = line.strip().split(", ")
            x_value = int(parts[0].split("+")[1])
            y_value = int(parts[1].split("+")[1])
            button_b.__init__(x_value, y_value)
        elif "Prize" in line:
            parts = line.strip().split(", ")
            x_value = int(parts[0].split("=")[1])
            y_value = int(parts[1].split("=")[1])
            prizes.__init__(x_value + 10000000000000, y_value + 10000000000000)
        else:
            min_cost = float('inf')
            
            # Berechnung des GCD für die x-Werte von Button A und Button B
            gcd, x, y = extended_gcd(button_a.x, button_b.x)
            print(prizes)
            print(gcd, x, y)
            
            # Überprüfen, ob es eine Lösung gibt
            if prizes.x % gcd != 0:
                continue  # Es gibt keine Lösung, wenn der GCD nicht teilt
            
            # Lösung finden und skalieren
            scale = prizes.x // gcd
            x *= scale
            y *= scale

            # Berechne die möglichen Lösungen
            remaining_y = prizes.y - x * button_a.y
            if remaining_y % button_b.y == 0:
                b_count = remaining_y // button_b.y
                if b_count >= 0:  # Stelle sicher, dass b_count nicht negativ ist
                    min_cost = min(min_cost, x * 3 + b_count * 1)

            if min_cost != float("inf"): count += min_cost

    return count


print("First Gold Star:", firstGoldStar(lines))
print("Second Gold Star:", secondGoldStar(lines))




