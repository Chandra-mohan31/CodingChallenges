public class Tree {
    static class Node {
        int value;
        Node left, right;

        Node(int value) {
            this.value = value;
            left = null;
            right = null;
        }
    }

    public void insert(Node node, int value) {
        if (value < node.value) {
            if (node.left != null) {
                insert(node.left, value);
            } else {
                System.out.println("iserted  to left of" + node.value);
                node.left = new Node(value);
            }
        } else if (value > node.value) {
            if (node.right != null) {
                insert(node.left, value);
            } else {
                System.out.println("inserted to right of" + node.value);
                node.right = new Node(value);
            }

        }

    }

    public void traverseInOrder(Node node) {
        if (node != null) {
            traverseInOrder(node.left);
            System.out.println(node.value);
            traverseInOrder(node.right);
        }
    }

    public static void main(String[] args) {
        Tree tree = new Tree();
        Node root = new Node(5);
        tree.insert(root, 2);
        tree.insert(root, 7);
        tree.traverseInOrder(root);
    }
}