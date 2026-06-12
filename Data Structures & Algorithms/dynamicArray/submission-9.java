class DynamicArray {
    private int[] storage;
    private TreeSet<Integer> usedIndices;

    public DynamicArray(int capacity) {
        storage = new int[capacity];
        usedIndices = new TreeSet<Integer>();
    }

    public int get(int i) {
        return storage[i];
    }

    public void set(int i, int n) {
        System.out.println("Setting %d to %d".formatted(i, n));
        if (!usedIndices.contains(i)) 
            usedIndices.add(i);
        else System.out.println("skipping index");
        storage[i] = n;
    }

    public void pushback(int n) {
        System.out.println("Pushing %d, used %d, length %d".formatted(n, usedIndices.size(), storage.length));
        if (usedIndices.size() == 0) {
            set(0, n);
            return;
        }
        int highestUsedIndex = usedIndices.last();
        if (storage.length == highestUsedIndex + 1) {
            System.out.println("Doubling size from %d".formatted(storage.length));
            resize();
        }
        set(highestUsedIndex + 1, n);
    }

    public int popback() {
        System.out.println(Arrays.toString(usedIndices.toArray()));
        System.out.println(Arrays.toString(storage));
        int poppedIndex = usedIndices.last();
        usedIndices.remove(poppedIndex);
        int poppedValue = storage[poppedIndex];
        storage[poppedIndex] = 0;
        return poppedValue;
    }

    private void resize() {
        int[] oldStorage = storage;
        storage = new int[storage.length * 2];

        for (int i = 0; i < oldStorage.length; i++) {
            storage[i] = oldStorage[i];
        }
        System.out.println("Old array: %s".formatted(Arrays.toString(oldStorage)));
        System.out.println("New array: %s".formatted(Arrays.toString(storage)));
    }

    private void setSize(int newSize) {
    }

    public int getSize() {
        return usedIndices.size();
    }

    public int getCapacity() {
        return storage.length;
    }
}
