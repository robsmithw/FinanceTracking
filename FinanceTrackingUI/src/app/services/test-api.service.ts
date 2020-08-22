import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { API_URL } from '../../environments/environment';
import { Test } from '../models/test.model';

@Injectable()
export class TestApiService {

    constructor(private httpClient: HttpClient) {
    }

    public errorHandler(error: HttpErrorResponse){
        if (error.error instanceof HttpErrorResponse) {
        // A client-side or network error occurred.
            console.error('An error occurred:', error.error.message);
        } else {
            // The backend returned an unsuccessful response code.
            console.error(
                `Backend returned code ${error.status}, ` +
                `body was: ${error.error}`);
        }
        // Return an observable with a error message.
        return throwError('Error occured; please try again later.');
    }

    // GET test records
    getTest(): Observable<Test[]> {
        return this.httpClient.get<Test[]>(`${API_URL}/tests`)
            .pipe(catchError(this.errorHandler));
    }
}
