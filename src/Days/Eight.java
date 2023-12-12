package Days;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Eight {

    static HashMap<String, String[]> searchMap = new HashMap<>();
    static String pattern;

    public static void main(String[] args) {

        String filePath = "C:\\Users\\Timo\\IdeaProjects\\AdventOfCode2023\\src\\InputFiles\\input_test";

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

//        System.out.println("Part one: " + partOne());
        System.out.println(partTwo());
    }

    private static int partTwo() {
        int result = 0;
        List<String> addList = new ArrayList<>();
        for (String entry : searchMap.keySet()) {
            if (entry.charAt(2) == 'A') {
                addList.add(entry);
            }
        }
        String[] keyList = addList.toArray(new String[0]);
        while (true) {
            boolean endZ = true;
            for (int i = 0 ; i < pattern.length(); i++) {
                char currentDir = pattern.charAt(i);

                for (int j = 0; j < keyList.length; j ++) {
                    String[] list = searchMap.get(keyList[j]);

                    if (currentDir == 'L') {
                        keyList[j] = list[0];
                    } else {
                        keyList[j] = list[1];
                    }
                }
                result++;
                System.out.println(Arrays.toString(keyList));

                for (String key : keyList) {
                    if (key.charAt(2) != 'Z') {
                        endZ = false;
                        break;
                    }
                }
                if (endZ) break;
            }
            if (endZ) break;

        }
        return result;
    }


    private static int partOne() {
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

        return steps;
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
