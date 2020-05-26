
!+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+//
!                                                                                                                                       //
! mc.f                                                                                                                                  //
!                                                                                                                                       //
! D. C. Groothuizen Dijkema - January, 2020                                                                                             //
!+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+//

! Approximating mathematical constants with Monte Carlo methods


module monte_carlo
  implicit none
  ! please ignore the incongruity of having both an analytical definition of pi to use in one function, and another function to calculate
  ! the value of pi itself
  real(kind=8), parameter :: pi=4.*atan(1.)
contains

  function simulate_e() result(cnt)
    !
    ! Count the number of uniformly distributed random real numbers on [0,1] which are needed for their sum to become strictly greater than
    ! one.
    ! Euler's number is the expected value of this function.
    !
    ! Returns
    ! -------
    ! cnt : integer
    !   - The count of random numbers.
    !

    integer :: cnt
    real(kind=8) :: sum,rand_num

    cnt=0
    sum=0.
    ! produce the count
    do while (sum.LE.1)
      call random_number(rand_num)
      sum=sum+rand_num
      cnt=cnt+1
    end do
  end function simulate_e

  function simulate_pi() result(within)
    !
    ! Randomly generate a point in the unit square and determine if it falls within the unit circle.
    !
    ! Returns
    ! -------
    ! within : integer
    !   - 1 if the randomly generated point is within the unit circle, 0 otherwise. This should be a logical, but using an integer allows
    !     simple addition.
    !
    integer :: within

    real(kind=8) :: distance
    real(kind=8), dimension(2) :: point

    ! determine the point and its distance to the origin
    call random_number(point)
    distance=point(1)**2+point(2)**2

    if (distance.LE.1) then
      within=1
    else
      within=0
    end if
  end function simulate_pi

  function simulate_chord_length() result(distance)
    !
    ! Randomly generate a point on the radius of the unit circle, and determine its distance to the point (1,0). This is, 
    ! effectively, the distance between any two random points, as those points could be rotated until one of them was (1,0)
    !
    ! Returns
    ! -------
    ! distance : real(kind=8)
    !   - The chord length of two random points on the unit circle.
    !
    real(kind=8) :: distance,angle

    call random_number(angle)
    ! the range [0,1] to [0,2*pi]
    angle=angle*2.*pi
    distance=2.*sin(0.5*angle) ! formula derived simply from the definition of the sine function
  end function simulate_chord_length

  subroutine approximate_e(n_itr,means)
    !
    ! Use Monte Carlo simulations to produce successfully more accurate approximations of Euler's number.
    !
    ! Parameters
    ! ----------
    ! n_itr : integer, intent(in)
    !   - The number of simulations to run.
    ! means : real(kind=8), intent(inout), dimension(n_itr)
    !   - The array in which to store the moving mean of the simulations.
    !
    integer, intent(in) :: n_itr
    real(kind=8), intent(inout), dimension(n_itr) :: means

    real(kind=8) :: mean
    integer :: itr,approx

    ! initialise the mean
    mean=simulate_e()
    means(1)=mean
    ! produce a sample, update the moving mean, and output
    do itr=2,n_itr
      approx=simulate_e()
      mean=mean+(approx-mean)/(itr+1)
      means(itr)=mean
    end do
  end subroutine approximate_e

  subroutine approximate_pi_integration(n_itr,means)
    !
    ! Use Monte Carlo simulations to produce successfully more accurate approximations of pi.
    !
    ! Parameters
    ! ----------
    ! n_itr : integer, intent(in)
    !   - The number of simulations to run.
    ! means : real(kind=8), intent(inout), dimension(n_itr)
    !   - The array in which to store the moving mean of the simulations.
    !
    integer, intent(in) :: n_itr
    real(kind=8), intent(inout), dimension(n_itr) :: means

    integer :: itr,cnt

    ! initialise
    cnt=0
    ! produce a sample, update the moving mean, and output
    do itr=1,n_itr
      cnt=cnt+simulate_pi()
      means(itr)=4*real(cnt)/itr
    end do
  end subroutine approximate_pi_integration

  subroutine approximate_pi_chord_length(n_itr,means)
    !
    ! Use Monte Carlo simulations to produce successfully more accurate approximations of pi.
    !
    ! Parameters
    ! ----------
    ! n_itr : integer, intent(in)
    !   - The number of simulations to run.
    ! means : real(kind=8), intent(inout), dimension(n_itr)
    !   - The array in which to store the moving mean of the simulations.
    !
    integer, intent(in) :: n_itr
    real(kind=8), intent(inout), dimension(n_itr) :: means

    real(kind=8) :: mean,approx
    integer :: itr

    ! initialise
    mean=4/simulate_chord_length()
    means(1)=mean
    ! produce a sample, update the moving mean, and output
    do itr=2,n_itr
      approx=simulate_chord_length()
      mean=mean+(approx-mean)/(itr+1)
      means(itr)=4/mean
    end do
  end subroutine approximate_pi_chord_length

end module monte_carlo
