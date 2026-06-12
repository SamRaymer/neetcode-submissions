class Deque {
    Node leftMost;
    Node rightMost;
    class Node {
        Node(int val) {
            value = val;
        }
        Node left;
        Node right;
        int value;
    }

    public Deque() {
    }


    public boolean isEmpty() {
        return this.leftMost == null;
    }

    public void append(int value) {
        Node toAppend = new Node(value);
        if (this.isEmpty()) {
            this.leftMost = toAppend;
            this.rightMost = toAppend;
            return;
        }

        toAppend.left = this.rightMost;
        this.rightMost.right = toAppend;
        this.rightMost = toAppend;
    }

    public void appendleft(int value) {
        Node toAppend = new Node(value);
        if (this.isEmpty()) {
            this.leftMost = toAppend;
            this.rightMost = toAppend;
            return;
        }

        toAppend.right = this.leftMost;
        this.leftMost.left = toAppend;
        this.leftMost = toAppend;
    }

    public int pop() {
        if (this.isEmpty()) return -1;
        
        Node popped = this.rightMost;
        this.rightMost = popped.left;
        if (this.rightMost == null) {
            this.leftMost = null;
        } else {
            this.rightMost.right = null;
        }
        return popped.value;
    }

    public int popleft() {
        if (isEmpty()) return -1;
        
        Node popped = this.leftMost;
        this.leftMost = popped.right;
        if (this.leftMost == null) {
            this.rightMost = null;
        } else {
            this.leftMost.left = null;
        }
        return popped.value;
    }
}
