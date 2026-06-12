class LinkedList {

    class Node {
        int value;
        Node next;
    }
    Node head;
    int length = 0;

    public LinkedList() {

    }

    private Node getNode(int index){
        Node current = head;
        for (int i = 0; i < index; i++) {
            System.out.println("moving past %d".formatted(current.value));
            current = current.next;
        }
        return current;
    }

    public int get(int index) {
        if (index >= length) {
            return -1;
        }
        Node result = getNode(index);
        return result.value;
    }

    public void insertHead(int val) {
        Node toInsert = new Node();
        toInsert.value = val;
        toInsert.next = head;
        head = toInsert;
        length++;
    }

    public void insertTail(int val) {
        if (length == 0) {
            insertHead(val);
            return;
        }

        Node toInsert = new Node();
        toInsert.value = val;

        Node parent = getNode(length - 1);
        parent.next = toInsert;
        length++;
    }

    public boolean remove(int index) {
        if (index >= length) return false;

        if (index > 0) {
            Node parent = getNode(index - 1);
            parent.next = parent.next.next;
        } else { // node to remove is head
            head = head.next;
        }
        length--;
        return true;
    }

    public ArrayList<Integer> getValues() {
        ArrayList<Integer> result = new ArrayList<Integer>();

        Node current = head;
        while (current != null) {
            result.add(current.value);
            current = current.next;
        }
        return result;
    }
}
