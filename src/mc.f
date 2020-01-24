
!+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+//
!                                                                                                                                       //
! mc.f                                                                                                                                  //
!                                                                                                                                       //
! D. C. Groothuizen Dijkema - January, 2020                                                                                             //
!+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+//

! Approximating mathematical constants with Monte Carlo methods

module monte_carlo
  implicit none
contains

  function simulate_e() result(cnt)
    ! Defines the function of which e is the expected value

    integer :: cnt
    real(kind=8) :: sum,rand_num

    cnt=0
    sum=0
    ! count the number of random numbers needed to sum to more than 1
    do while (sum.LE.1)
      call RANDOM_NUMBER(rand_num)
      sum=sum+rand_num
      cnt=cnt+1
    end do

  end function simulate_e

  function simulate_pi() result(within)

    logical :: within

    real(kind=8) :: distance
    real(kind=8), dimension(2) :: point

    call RANDOM_NUMBER(point)
    distance=point(1)**2+point(2)**2

    if (distance.LE.1) then
      within=.TRUE.
    else
      within=.FALSE.
    end if

  end function simulate_pi

  subroutine approximate_e(n_itr,means)
    !DEC$ ATTRIBUTES DLLEXPORT :: approximate_e
    !DEC$ ATTRIBUTES C :: approximate_e
    
    integer, intent(in) :: n_itr
    real(kind=8), intent(inout), dimension(n_itr) :: means

    real(kind=8) :: mean
    integer :: itr,approx

    ! produce a sample of the simulate_e() function and keep a running mean
    do itr=1,n_itr
      approx=simulate_e()
      if (itr.EQ.1) then
        mean=approx
      else
        ! update the mean
        mean=mean+(approx-mean)/(itr+1)
      end if
      means(itr)=mean
    end do

  end subroutine approximate_e

  subroutine approximate_pi(n_itr,means)
    !DEC$ ATTRIBUTES DLLEXPORT :: approximate_e
    !DEC$ ATTRIBUTES C :: approximate_e
    
    integer, intent(in) :: n_itr
    real(kind=8), intent(inout), dimension(n_itr) :: means

    integer :: itr,cnt

    cnt=0
    do itr=1,n_itr
      if (simulate_pi()) then
        cnt=cnt+1
      end if
      means(itr)=4*real(cnt)/itr
    end do
    
  end subroutine approximate_pi

end module monte_carlo
