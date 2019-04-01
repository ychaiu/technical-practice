// a class is a special function

class Rectangle {
    constructor(height,width) {
        this.height = height;
        this.width = width
    }
}

// // func declarations are HOISTED - using a variable before it is declared
// // class declarations are not - declare class first then use it

// //  unnamed class
// let Rectangle = class {
//     constructor(height,width) {
//         this.height = height;
//         this.width = widht;
//     }
// }

// // named class
// let Rectangle = class Rectangle2 {
//     constructor(height,width) {}
//         this.height = height;
//         this.width = width;
// }

apple = new Rectangle(10,20);
console.log(apple.height);