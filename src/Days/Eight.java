package Days;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.net.StandardSocketOptions;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Objects;
import java.util.Scanner;

public class Eight {

    static HashMap<String, String[]> searchMap = new HashMap<>();
    static String pattern;

    public static void main(String[] args) {

        String filePath = "C:\\Users\\Timo\\IdeaProjects\\AdventOfCode2023\\src\\InputFiles\\input_8";

        int count = 0;

        try (Scanner scanner = new Scanner(new File(filePath))) {

            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                if (count < 1) {
                    pattern = line;
                    count++;
                } else {
                    fillMap(line);
                }
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        String currentString = "AAA";
        int steps = 0;

        while (true) {
            for (int i = 0 ; i < pattern.length(); i++) {
                char currentDir = pattern.charAt(i);
                String[] list = searchMap.get(currentString);
                if (currentDir == 'L') {
                    currentString = list[0];
                } else {
                    currentString = list[1];
                }
                steps++;
                if (currentString.equals("ZZZ")) {
                    break;
                }
            }
            if (currentString.equals("ZZZ")) {
                break;
            }
        }

        System.out.println(steps);
    }


    private static void fillMap(String line) {
        String[] parts = line.split("\\W");
        ArrayList<String> patts = new ArrayList<>();
        for (String i : parts) {
            if (!Objects.equals(i, "")) {
                patts.add(i);
            }
        }
        searchMap.put(patts.get(0), new String[] {patts.get(1), patts.get(2)});
    }
}
