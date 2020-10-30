export class Transaction {
    
    public description: string;
    public amount: number;
    public date: Date;
    
    constructor(
      description: string,
      amount: number,
      date: string
    ) 
    {
        this.description = description;
        this.amount = amount;
        this.date = new Date(date);
    }
  }