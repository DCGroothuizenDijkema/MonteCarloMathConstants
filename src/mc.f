
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

    integer :: cnt
    real(kind=8) :: sum,rand_num

    cnt=0
    sum=0
    do while (sum.LE.1)
      call RANDOM_NUMBER(rand_num)
      sum=sum+rand_num
      cnt=cnt+1
    end do

  end function simulate_e

  subroutine approximate_e(n_itr,means)
    !DEC$ ATTRIBUTES DLLEXPORT :: approximate_e
    !DEC$ ATTRIBUTES C :: approximate_e
    implicit none
    integer, intent(in) :: n_itr
    real(kind=8), intent(inout), dimension(n_itr) :: means

  end subroutine approximate_e

end module monte_carlo
