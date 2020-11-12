import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { API_URL } from '../../environments/environment';
import { Transaction } from '../models/transaction.model';

@Injectable()
export class FileApiService {

    constructor(private httpClient: HttpClient) {
    }

    private options = { headers: new HttpHeaders().set('Content-Type', 'application/json') };

    public errorHandler(error: HttpErrorResponse){
        if (error.error instanceof HttpErrorResponse) {
        // A client-side or network error occurred.
            console.error('An error occurred:', error.error.message);
        } else {
            // The backend returned an unsuccessful response code.
            console.error(
                `Backend returned code ${error.status}, ` +
                `body was: ${error.error}`);
            console.log(error);
        }
        // Return an observable with a error message.
        return throwError('Error occured; please try again later.');
    }

    // GET template file
    getTemplate(): Observable<Blob> {
        return this.httpClient.get(`${API_URL}/downloadTemplate`, {responseType : 'blob'})
            .pipe(catchError(this.errorHandler));
    }
    uploadCsv(file: File): Observable<Transaction[]>{
        const formData: FormData = new FormData();
        formData.append('file', file, file.name);
        return this.httpClient.post<Transaction[]>(`${API_URL}/processCsv`, formData)
            .pipe(catchError(this.errorHandler));
    }
    saveTransactions(transactions: Transaction[]): Observable<Transaction[]> {
        return this.httpClient.post<Transaction[]>(`${API_URL}/saveTransactions`, transactions, this.options)
            .pipe(catchError(this.errorHandler));
    }
    getAllTransactions(): Observable<Transaction[]>{
        return this.httpClient.get<Transaction[]>(`${API_URL}/getAllTransaction`)
            .pipe(catchError(this.errorHandler));
    }
}
