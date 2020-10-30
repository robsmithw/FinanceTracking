import { Component, OnInit, OnDestroy} from '@angular/core';
import { Subscription } from 'rxjs';
import { saveAs } from 'file-saver';
import { Transaction } from './models/transaction.model';
import { ToastrService } from 'ngx-toastr';
import { FileApiService } from './services/file-api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'FinanceTracking';
  transactions: Transaction[];
  fileToProcess: File = null;
  fileProcessed: boolean = false;
  currentTransSaved: boolean = false;

  constructor(private fileApi: FileApiService, private toastr: ToastrService){

  }

  ngOnInit(){
  }

  downloadTemplate(){
    this.fileApi.getTemplate()
      .subscribe(
        res => {
          saveAs(res, 'template.csv');
          this.toastr.success('Successfully downloaded template');
        },
        err => {
          this.toastr.error(err);
        });
  }
  
  uploadFile() {
    if (this.fileToProcess === null) {
      this.fileProcessed = false;
      return;
    };

    console.log(this.fileToProcess);

    this.fileApi.uploadCsv(this.fileToProcess).subscribe((data: Transaction[]) => {
      this.transactions = data;
      this.fileProcessed = true;
      this.toastr.info("Successfully processed uploaded file.");
      console.log(data);
      this.fileToProcess = null;
    },
    err => {
      this.toastr.error(err);
    });
  }

  saveTransactions() {
    this.fileApi.saveTransactions(this.transactions).subscribe((data: any) => {
      this.currentTransSaved = true;
      this.toastr.success("Successfully saved all transactions shown.");
    },
    err => {
      this.toastr.error(err);
    });
  }

  handleFileInput(files: FileList) {
    this.fileToProcess = files.item(0);
  }

  ngOnDestroy(){
  }

}
